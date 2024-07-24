package Sep2024.ValidParentheses;

import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        final Stack<Character> openedBrackets = new Stack<>();

        for (char c:s.toCharArray()) {
            if (isOpener(c)) // if c in '([{'
                openedBrackets.push(c);
            else if (openedBrackets.isEmpty()
                    || (!matches(openedBrackets.pop(), c)))
                    return false;
        }

        return openedBrackets.isEmpty();
    }

    /**
     * whether c is one of "([{"
     * */
    public boolean isOpener(char c) {
        return c == '(' || c == '[' || c == '{';
    }

    /**
     * @return whether the opening character matches the closing character
     * */
    public boolean matches(char opener, char closer) {
        if (opener == '(')
            return closer == ')';
        if (opener == '[')
            return closer == ']';
        return closer == '}';
    }

    public static void main(String[] args) {
        System.out.println(new Solution().isValid("([)]"));
    }
}
