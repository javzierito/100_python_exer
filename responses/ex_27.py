def calc_aceleration(v_2: float,v_1: float, t_2: float, t_1:float) -> float:
    return (v_2-v_1)/(t_2-t_1)

print(calc_aceleration(v_2=10.0, v_1=0.0, t_2=20.0, t_1=0.0))