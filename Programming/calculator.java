class Calculator{
    public static int addition(int a,  int b){
        return a + b;
    }
    public static int subtraction(int a,  int b){
        return a - b;
    }
    public static int multiplication(int a,  int b){
        return a * b;
    }
    public static int division(int a,  int b){
        return a / b;
    }
    public static void main(String[] args){
        System.out.println("Addition of two numbers " +addition(2,3));
        System.out.println("Subtraction of two numbers " +subtraction(5,3));
        System.out.println("Multiplication of two numbers " +multiplication(2,3));
        System.out.println("Division of two numbers " +division(6,3));
    }
}