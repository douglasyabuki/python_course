# Positional-Only Parameters (/) and Keyword-Only Arguments (*)
# *args (unlimited positional arguments)
# **kwargs (unlimited keyword arguments)
# 🟢 Positional-only Parameters (/) - Everything before the slash must be ❗️POSITIONAL ONLY❗️.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * alone ❗️DOES NOT CAPTURE❗️ values.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def sum_(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


sum_(1, 2, c=3, name='test')
