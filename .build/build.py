#! /usr/bin/env python

import sys, os

if __name__ == "__main__":
    sys.argv[0] = 'rpython'  # required for sqpyte hacks

    if not any(arg.startswith("-") for arg in sys.argv):
        sys.argv.append("--batch")
    sys.argv.append(os.path.join(os.path.dirname(__file__), "..", "targetrsqueak.py"))
    import environment
    from rpython.translator.goal.translate import main
    main()
