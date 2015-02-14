# Write your MySQL query statement below
SELECT Department.Name as Department, Employee.Name as Employee, Employee.Salary as Salary FROM Employee
    INNER JOIN Department
        ON Employee.DepartmentId = Department.Id
    LEFT JOIN (SELECT DepartmentId, max(Salary) as maxSalary FROM Employee GROUP BY DepartmentId) as MaxSalaryPerDepartment
        ON Employee.DepartmentId = MaxSalaryPerDepartment.DepartmentId
    WHERE Employee.Salary >= MaxSalaryPerDepartment.maxSalary;