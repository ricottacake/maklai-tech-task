#### **Approach**
The main idea of this algorithm is to sift out unsuitable trees, and then check the remaining trees using regular expressions. This will make it easy to change or add criteria for tree selection if needed later, simply by changing the current regular expression or creating a new regular expression.

#### **The algorithm is divided into two parts**
1. Searching for trees that meet the criteria
2. Search for all possible combinations of permutations of elements of this tree according to the conditions (`mix_algorithm` function)

#### How run and test?
1. Install python and pip for your OS
2. Clone repository
`git clone https://github.com/ricottacake/maklai-tech-task.git`
3. Go to project folder
4. Install dependencies
`pip install -r requirements.txt`
5. Run via FastAPI
`python3 -m uvicorn main:app --reload`
6. Test
http://127.0.0.1:8000/paraphrase?tree=*TREE*

#### Example

http://127.0.0.1:8000/paraphrase?tree=%28S%20%28NP%20%28NP%20%28DT%20The%29%20%28JJ%20charming%29%20%28NNP%20Gothic%29%20%28NNP%0A%20Quarter%29%20%29%20%28%2C%20%2C%29%20%28CC%20or%29%20%28NP%20%28NNP%20Barri%29%20%28NNP%20G%C3%B2tic%29%20%29%20%29%20%28%2C%20%2C%29%20%28VP%20%28VBZ%20has%29%20%28NP%20%28NP%0A%20%28JJ%20narrow%29%20%28JJ%20medieval%29%20%28NNS%20streets%29%20%29%20%28VP%20%28VBN%20filled%29%20%28PP%20%28IN%20with%29%20%28NP%20%28NP%20%28JJ%0A%20trendy%29%20%28NNS%20bars%29%20%29%20%28%2C%20%2C%29%20%28NP%20%28NNS%20clubs%29%20%29%20%28CC%20and%29%20%28NP%20%28JJ%20Catalan%29%20%28NNS%0A%20restaurants%29%20%29%20%29%20%29%20%29%20%29%20%29%20%29
