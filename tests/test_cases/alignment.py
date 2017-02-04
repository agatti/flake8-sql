query = """SELECT abc
           FROM xyz
           WHERE def = 'def'"""  # Q447
query = """SELECT abc
             FROM xyz
            WHERE def = 'def'"""
query = """SELECT abc
             FROM xyz
            WHERE def = 'def' AND feg = 'feg'"""  # Q445
query = """SELECT abc
             FROM xyz
            WHERE def = 'def'
              AND feg = 'feg'
               OR ijk = 'ijk'"""
query = """INSERT INTO xyz (clm1, clm2)
                VALUES (abc, def)"""  # Q447
query = """INSERT INTO xyz (clm1, clm2)
           VALUES (abc, def)"""
query = """INSERT INTO xyz (clm1, clm2)
                       SELECT abc
                       FROM def"""  # Q447
query = """SELECT abc
             FROM xyz
           JOIN ghj ON jkl = def
            WHERE def = 'def'"""  # Q447
