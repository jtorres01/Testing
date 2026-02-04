class Solution:

    def fizzBuzz( n: int) -> List[str]:
        answer = [i+1 for i in range(n)]
        string = "FizzBuzz"

        for i in range(n):
            if (answer[i] % 3 == 0) and (answer[i] % 5 == 0):
                answer[i] = string
            elif (answer[i] % 3 == 0):
                answer[i] = "Fizz"
            elif(answer[i] % 5 == 0):
                answer[i] = "Buzz"
        return answer 

    
    def myFizzBuzz(n):
        result = []
        for i in range(n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        
        return result        

    answer = [i+1 for i in range(15)]
    print(answer)
    
    print(myFizzBuzz(15))
