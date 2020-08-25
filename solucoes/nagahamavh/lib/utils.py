def sort_dict(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}


def head_dict(d, n):
    from itertools import islice
    return dict(islice(d.items(), n))
