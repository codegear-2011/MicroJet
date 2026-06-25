"""
MicroJet Template Engine
========================

Syntax:
    <%jp expression %>          → Python expression output
    <%jp: statement %>          → Python block (if / for / while / with)
    <%jp: elif condition %>     → elif branch
    <%jp: else %>               → else branch
    <%jp: end %>                → close a block
    {# comment #}               → template comment (removed from output)

Example (.html file):
    <h1>Hello, <%jp name %>!</h1>

    <%jp: for item in items %>
        <li><%jp item.upper() %></li>
    <%jp: end %>

    <%jp: if user_is_admin %>
        <span>Admin Panel</span>
    <%jp: elif user_is_staff %>
        <span>Staff Area</span>
    <%jp: else %>
        <span>Welcome</span>
    <%jp: end %>
"""

import re
import os
import builtins


# ── Regex Patterns ────────────────────────────────────────────────────────────

_RE_COMMENT = re.compile(r'\{#.*?#\}', re.DOTALL)
_RE_BLOCK   = re.compile(r'<%jp:(.*?)%>', re.DOTALL)
_RE_EXPR    = re.compile(r'<%jp\s+(.*?)%>', re.DOTALL)
_RE_TAG     = re.compile(r'(<%jp:.*?%>|<%jp\s+.*?%>)', re.DOTALL)


# ── Tokeniser ─────────────────────────────────────────────────────────────────

def _tokenise(source: str) -> list:
    """
    Returns a list of (kind, value) tuples.
    kind is one of: 'text' | 'expr' | 'block'
    """
    source = _RE_COMMENT.sub('', source)
    tokens = []

    for part in _RE_TAG.split(source):
        if not part:
            continue

        block_m = _RE_BLOCK.fullmatch(part.strip())
        expr_m  = _RE_EXPR.fullmatch(part.strip())

        # Need to match on the original part, not stripped (to preserve text whitespace)
        block_m2 = _RE_BLOCK.fullmatch(part)
        expr_m2  = _RE_EXPR.fullmatch(part)

        if block_m2:
            tokens.append(('block', block_m2.group(1).strip()))
        elif expr_m2:
            tokens.append(('expr', expr_m2.group(1).strip()))
        else:
            tokens.append(('text', part))

    return tokens


# ── Code Generator ────────────────────────────────────────────────────────────

_BLOCK_OPENERS = ('if ', 'for ', 'while ', 'with ', 'try:', 'try')
_BRANCH_WORDS  = ('else', 'else:', 'elif ')
_CLOSER        = ('end', 'end ')


def _generate(tokens: list) -> str:
    """
    Convert tokens into a Python function source string.
    The function signature is:  _render(__ctx: dict) -> str
    Context variables are available directly by name inside templates.
    """
    lines = [
        "def _render(__ctx):",
        "    __out = []",
    ]

    depth = 1  # current indentation level (1 = inside function)
    pad   = lambda d: "    " * d

    for kind, value in tokens:

        if kind == 'text':
            # Use repr() so any special chars are safely escaped
            lines.append(f"{pad(depth)}__out.append({repr(value)})")

        elif kind == 'expr':
            lines.append(f"{pad(depth)}__out.append(str({value}))")

        elif kind == 'block':
            stmt = value

            if stmt in _CLOSER:
                depth = max(1, depth - 1)

            elif stmt in ('else', 'else:'):
                # step out, write else:, step back in
                depth = max(1, depth - 1)
                lines.append(f"{pad(depth)}else:")
                depth += 1

            elif stmt.startswith('elif '):
                depth = max(1, depth - 1)
                cond = stmt if stmt.endswith(':') else stmt + ':'
                lines.append(f"{pad(depth)}{cond}")
                depth += 1

            else:
                # Normal opener
                opener = stmt if stmt.endswith(':') else stmt + ':'
                lines.append(f"{pad(depth)}{opener}")
                depth += 1

    lines.append(f"    return ''.join(__out)")
    return '\n'.join(lines)


# ── Executor ──────────────────────────────────────────────────────────────────

def _execute(py_source: str, context: dict) -> str:
    """
    Compile and run the generated Python function.
    Context variables are injected into the function's global namespace
    so they resolve by bare name (e.g. <%jp name %> not <%jp ctx['name'] %>).
    """
    # Build a globals dict: builtins + context variables
    ns = vars(builtins).copy()
    ns.update(context)

    exec(compile(py_source, '<microjet-template>', 'exec'), ns)
    return ns['_render'](context)


# ── Public API ────────────────────────────────────────────────────────────────

def render_string(source: str, **context) -> str:
    """Render a template from a raw string."""
    tokens   = _tokenise(source)
    py_src   = _generate(tokens)
    return _execute(py_src, context)


def debug_compile(source: str) -> str:
    """Return the generated Python source (useful for debugging)."""
    return _generate(_tokenise(source))


class TemplateEngine:
    """
    File-based template renderer for MicroJet.

    Usage:
        engine = TemplateEngine("templates")
        html   = engine.render("index.html", title="Home", items=[1, 2, 3])
    """

    def __init__(self, template_dir: str = "templates"):
        self.template_dir = template_dir

    def render(self, template_name: str, **context) -> str:
        """Render a template file with the given context variables."""
        path = os.path.join(self.template_dir, template_name)

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"[MicroJet] Template not found: '{path}'\n"
                f"  template_dir = '{self.template_dir}'\n"
                f"  file         = '{template_name}'"
            )

        with open(path, encoding='utf-8') as fh:
            source = fh.read()

        tokens = _tokenise(source)
        py_src = _generate(tokens)
        return _execute(py_src, context)

    def render_string(self, source: str, **context) -> str:
        return render_string(source, **context)

