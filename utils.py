def pdb():
    """Enter pdb in App Engine. Renable system streams for it."""
    import pdb
    import sys
    pdb.Pdb(stdin=getattr(sys,'__stdin__'),stdout=getattr(sys,'__stderr__')).set_trace(sys._getframe().f_back)
