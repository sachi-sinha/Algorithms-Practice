import javax.swing.*;

public class StackLL {
    protected SLinkedList S;

    public StackLL(){
        S = new SLinkedList();
    }

    public boolean isEmpty(){
        return S.isEmpty();
    }

    public long size(){
        return S.size();
    }

    public void push(Object element){
        S.insertHead(element);
    }

    public Object pop(){

        if (isEmpty()){
            JOptionPane.showMessageDialog(null, "Error! Stack is empty.");
            return null;
        }

        S.gotoHead();
        Object element = S.getCurr();

        S.deleteHead();
        return element;
    }

    public Object top(){

        S.gotoHead();
        return S.getCurr();

    }

}
