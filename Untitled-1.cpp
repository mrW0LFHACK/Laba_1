#include <iostream>
#include <vector>

using namespace std;

void printArray(const vector<int>& arr, int step) {
    cout << "Шаг " << step << ": ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    int step = 1;

    for (int i = 0; i < n - 1; i++) {
       
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

       
        if (min_idx != i) {
            swap(arr[i], arr[min_idx]);
        }


        printArray(arr, step);
        step++;
    }
}

int main() {
    vector<int> arr = {64, 25, 12, 22, 11};

    cout << "Исходный массив: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl << endl;

    selectionSort(arr);

    cout << endl << "Отсортированный массив: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
