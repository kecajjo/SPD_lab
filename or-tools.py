from ortools.linear_solver import  pywraplp



if __name__ == "__main__":
    solver = pywraplp.Solver.CreateSolver('GLOP')


    x = solver.NumVar(0,1,'x')
    y = solver.NumVar(0,2,'y')

    print('Number of variables = ', solver.NumVariables())

    #teraz robimy ograniczenie w postaci 0<= x +y <= 2
    ct = solver.Constraint(0,2,'ct')
    ct.SetCoefficient(x,1)
    ct.SetCoefficient(y,1)

    print('Number of contraints = ',solver.NumConstraints())

    #teraz stworzymy zaleznnosc ktora chcemy maksymalizowac
    # 3*x+y
    objective = solver.Objective()
    objective.SetCoefficient(x,3)
    objective.SetCoefficient(y,1)
    objective.SetMaximization()

    solver.Solve()
    print('Solution:')
    print('Objective value = ',objective.Value() )
    print('x = ',x.solution_value())
    print('y = ',y.solution_value())
