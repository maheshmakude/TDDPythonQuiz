"""
Q1. Why is the report method untestable ? [2 pts]

Ans - 
     1. As the  file path is user/OS/System specific
      2. inputs  to report method  depends on colabrataive (Range)
	 3. While writing  msg to a report file its constructed  from numbers.
	 4. it is easy to use for writer but not to user who is  using it.



Q2. How will you change the api of the report method to make it more testable ? [2 pts]

Ans :-
     1. For handelling the file pale we wili use file handler 

"""
class FizzBuzz(object):
    def report(self, numbers):

        report_file = open('c:/temp/fizzbuzz_report.txt', 'w')

        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                msg += "buzz "
                fizzbuzz_found = True

            if fizzbuzz_found:
                report_file.write(msg + "\n")

        report_file.close()

if "__main__" == __name__:
    fb = FizzBuzz()
    fb.report(range(100))

            
