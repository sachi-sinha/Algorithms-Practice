import javax.swing.*;

public class QueueLL {

    protected SLinkedList Q;

    public QueueLL(){
        Q = new SLinkedList();
    }

    public boolean isEmpty(){
        return Q.isEmpty();
    }

    public long size(){
        return Q.size();
    }

    public void enqueue(Object element){
        Q.gotoTail();
        Q.insertNext(element);
    }

    public Object dequeue(){
        if(isEmpty()){
            JOptionPane.showMessageDialog(null, "Error! Queue is empty.");
            return null;
        }
        Q.gotoHead();
        Object element = Q.getCurr();
        Q.deleteHead();
        return element;
    }

    public Object front(){
        if(isEmpty()){
            JOptionPane.showMessageDialog(null, "Error! Queue is empty.");
            return null;
        }
        Q.gotoHead();
        return Q.getCurr();
    }
}
