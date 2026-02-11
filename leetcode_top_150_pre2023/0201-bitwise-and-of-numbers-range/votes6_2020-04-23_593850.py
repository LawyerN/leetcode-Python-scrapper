class Solution {
    fun rangeBitwiseAnd(i_: Int, j_: Int): Int {
        var (t, i, j) = Triple(0, i_, j_)
        var ok = { lo: Long, hi: Long -> lo <= Math.min(i, j) && Math.max(i, j) < hi }
        (30 downTo 0).forEach{
            var lo = 1L shl it
            var hi = lo shl 1
            if (ok(lo, hi)) {
                t += lo.toInt()
                i -= lo.toInt()
                j -= lo.toInt()
            }
        }
        return t
    }
}