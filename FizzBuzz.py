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

    answer = [i+1 for i in range(15)]
    print(answer)
    
    #print(fizzBuzz(15))

        