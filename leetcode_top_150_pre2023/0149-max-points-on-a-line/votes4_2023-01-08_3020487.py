class Solution {
public:
int maxPoints(vector<vector<int>>& points) {
        int size=points.size(), count=1;
        for(int i=0;i<size;i++){
            unordered_map<double,int>um; // Cretaing HashMap
            double slope;
            for(int j=i+1;j<size;j++){
                if(points[j][0]-points[i][0]==0) //Checking if the slope is perpendicular or not as the x2-x1 == 0 defines slope is at 90 degree
                    slope=10001.00;
                else{
                    slope=double(points[j][1]-points[i][1])/double(points[j][0]-points[i][0]); // Using two-point form
                }
                um[slope]++; //  Using map to store the slope count with respect to a single point
            }
            for(auto k:um){ //Counting the maximum count of slope
                count=max(count,k.second+1); // Here we\'re adding 1 to include the point points[i] itself.
            }
        }
        return count;
    }
};