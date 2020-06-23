# Wrapper for Modifications 

The wrapper is written to make modifications to Google's differential privacy tool in order to improve performance overhead and simultaneously also try to obtain more accurate results.

Modifications made include:
    
    Parser for conversion of normal SQL queries to intrinsically private queries by:
        Converting normal SQL aggrregations to ANON aggregate functions
        Converting WHERE clauses to corresponding INNER JOIN clauses
    
    Algorithms to improve performance:
        Fast Bounded (assumes lower and upper bounds to be MIN and MAX respectively)
        Widened Winsorized (extended IQR values taken as respective lower and upper bounds)
    
