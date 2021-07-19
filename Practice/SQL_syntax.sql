SELECT * FROM Customers WHERE Last_Name='Smith';

+---------+-----------+------------+
  | Cust_No | Last_Name | First_Name |
  +---------+-----------+------------+
  | 1001    | Smith     | John       |
  | 2039    | Smith     | David      |
  | 2098    | Smith     | Matthew    |
  +---------+-----------+------------+
  3 rows in set (0.05 sec)
  
SELECT Cust_No, First_Name FROM Customers WHERE Last_Name='Smith';
  
  +---------+------------+
  | Cust_No | First_Name |
  +---------+------------+
  | 1001    | John       |
  | 2039    | David      |
  | 2098    | Matthew    |
  +---------+------------+
  3 rows in set (0.05 sec)
  
SELECT First_Name, Nickname FROM Friends WHERE Nickname LIKE '%brain%';

  +------------+------------+
  | First_Name | Nickname   |
  +------------+------------+
  | Ben        | Brainiac   |
  | Glen       | Peabrain   |  
  | Steven     | Nobrainer  |
  +------------+------------+
  3 rows in set (0.03 sec)

SELECT * FROM Friends WHERE First_Name LIKE '_en';

+------------+------------+-----------+
  | First_Name | Last_Name  | Nickname  |
  +------------+------------+-----------+
  | Ben        | Smith      | Brainiac  |
  | Jen        | Peters     | Sweetpea  |  
  +------------+------------+-----------+
  2 rows in set (0.03 sec)
