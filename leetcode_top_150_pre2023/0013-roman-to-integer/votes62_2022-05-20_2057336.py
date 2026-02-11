class Solution {
    fun romanToInt(s: String): Int {
        // 1. Create a Map for Roman Numeral Values
        val translations = mapOf(
            "I" to 1,
            "V" to 5,
            "X" to 10,
            "L" to 50,
            "C" to 100,
            "D" to 500,
            "M" to 1000
        )

        // 2. Preprocess the Input String (Subtractive Notation Handling)
        var modifiedString = s 
            .replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")

        // 3. Initialize the Result Variable
        var number = 0

        // 4. Iterate Through the String and Sum Values
        for (char in modifiedString) {
            number += translations.getValue(char.toString()) // Get value from map and add to total
        }

        // 5. Return the Final Result
        return number
    }
}