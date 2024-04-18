이전에 C++로 풀어본적 있는 문제
그러나 C++로는 일부 테스트에서 통과하지 못했다.

## 당시 C++ 코드
```#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int a = array.size() / 2;
    
    // write array numbers here
    for(int i = 0; i < array.size(); ++i)
    {
        if(array[i] >= array[i+1])
        {
            int b = array[i];
            array[i] = array[i+1];
            array[i+1] = b;
            --i;
        }
    }
    
    return array[a];
}```

하지만 다시 풀었을 때는 Python으로 다시 시도
Python의 경우 5분도 안지나서 문제 해결