"""
Day 7 — Text is data  (45-minute day: orientation week)
========================================================
The cleaning sequence, in order:
  strip -> case -> remove noise -> collapse whitespace -> convert -> validate
"""

# 1 -- Normalise a product name using the full sequence.
#      "  ACME   Tea®  1KG \n"  ->  "acme tea 1kg"
def ex_01(raw="  ACME   Tea®  1KG \n"):
    pass


# 2 -- Word frequency, case-insensitive, punctuation ignored. Return top 3.
PARA = """Data is messy. Data is always messy; cleaning data is most of the job.
          Anyone who says data is clean has not seen the data."""

def ex_02(text=PARA):
    pass


# 3 -- "1,250.00 PKR" -> 1250.0   Handle "  540 ", "N/A", "" as well.
def ex_03(value="1,250.00 PKR"):
    pass


# 4 -- First non-repeating character. Return None if there is none.
def ex_04(text="swiftbase"):
    pass


# 5 -- camelCase -> snake_case.  'totalRevenuePKR' -> 'total_revenue_pkr'
#      You need this on Day 33 for cleaning column names.
def ex_05(name="totalRevenuePKR"):
    pass


# 6 -- Anagram check, TWO ways: sorting, and counting.
#      Comment on which is cheaper for long strings and why.
#      ANSWER:
def ex_06_sorted(a="listen", b="silent"):
    pass

def ex_06_counted(a="listen", b="silent"):
    pass


# 7 -- THE REAL ONE.
# Collapse these to four canonical city names. Return {raw: canonical}.
# Then answer in a comment: which entries could NOT be fixed by a rule,
# and what does that imply about automating data cleaning?
# ANSWER:
RAW_CITIES = [
    "Lahore", "  lahore ", "LAHORE",
    "Karachi", "karachi  ", "KARACHI CITY",
    "Hyderabad", "hyderabad",
    "Islamabad", "Islamabd",
]

def ex_07(raw=RAW_CITIES):
    pass


# MINI ASSESSMENT -- from memory, 3 minutes
# "  ACME  Tea  1KG , 4 , 1,250.00 PKR "  ->  ("acme tea 1kg", 4, 1250.0)
def mini(line="  ACME  Tea  1KG , 4 , 1,250.00 PKR "):
    pass


if __name__ == "__main__":
    print(ex_01())
    print(ex_02())
    print(ex_03())
    print(ex_05())
    print(ex_07())
    print(mini())
