import pickle

pickle_in=open("outB_26200428_405_table.pickle","rb")
#pickle_in=open("DB_27654921.pickle","rb")
DB=pickle.load(pickle_in)
pickle_in.close()


pickle_in=open("outB_27654921_405_table.pickle","rb")
#pickle_in=open("DB_27654921.pickle","rb")
DB1=pickle.load(pickle_in)
pickle_in.close()


def merge(a, b, path=None):
    "merges b into a"
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]

merge(DB,DB1)


pickle_out=open("bOPmerge","wb")
pickle.dump(DB,pickle_out)
pickle_out.close()
