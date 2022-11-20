from skll.metrics import kappa

rater1 = [0, 1, 1, 2, 2, 0, 2, 2, 1, 3]
rater2 = [1, 2, 2, 3, 3, 0, 2, 2, 1, 3]
matrix = [[0, 0.33, 0.67, 1],
[0.33, 0, 0.33, 0.67],
[0.67, 0.33, 0, 0.33],
[1, 0.67, 0.33, 0]]

print(kappa(rater1,rater2))
print(kappa(rater1,rater2,'linear'))
print(kappa(rater1,rater2,matrix))
print(kappa(rater1,rater2,allow_off_by_one=True))