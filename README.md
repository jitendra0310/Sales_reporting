# Python exercise

Please submit your solution as a [git bundle](https://git-scm.com/docs/git-bundle)
attached in to the reply mail to our HR department. Please do not post
your solution publicly, do not create a public github repo with your
solution.

## General considerations

Feel free to use any Python version.

Feel free to use any module from the Python standard library, but don't use any
third party libraries (like pandas, toolz or sqlite).

Feel free to add in the code any extra comments you consider convenient. For
example, simplifications taken (if any) and their caveats, considerations about
computational complexity, etc.

Code cleanness, clarity, structure and presence of unit tests will be taken into
account when evaluating the solution.

## Input data

For the exercises we are going to be using two CSV files: `customers.csv` and
`sales.csv`. In DataWarehouse nomenclature, we could consider `customers.csv` to
be a dimension table, and `sales.csv` to be a fact table. Going with that
consideration, we can assume there is a *foreign key* constraint on
`customer_id`, so that we cannot have any sales measurements for customers that
are not contained in the `customers.csv` table.

## Task

Create a Python module `sales_per_customer.py` that, given the input
`customers.csv` and `sales.csv` files described above, generates a report with
"the total sales per customer". In particular, it should create an output file
`sales_per_customer.csv` such that:

* It is a valid CSV file.
* Has a header row with the following names: `name`, `email`, `address`,
  `sum(quantity)`.
* Each row contains information about a single customer.
* The row order is not important.
