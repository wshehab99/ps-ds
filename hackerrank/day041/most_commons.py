from collections import Counter
if __name__ == '__main__':
    s = sorted(input().strip())
    sc=Counter(s).most_common()
    sc=sc[:3]
    for item in sc:
        print(f"{item[0]} {item[1]}")
