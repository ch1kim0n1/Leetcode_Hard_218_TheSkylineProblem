class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> events;

        for (auto& b : buildings) {
            events.push_back({b[0], -b[2], b[1]});
            events.push_back({b[1], 0, 0});
        }

        sort(events.begin(), events.end());

        vector<vector<int>> ans;
        priority_queue<pair<int, int>> pq;
        pq.push({0, INT_MAX});

        for (auto& e : events) {
            int x = e[0];
            int h = e[1];
            int r = e[2];

            if (h < 0) {
                pq.push({-h, r});
            }

            while (!pq.empty() && pq.top().second <= x) {
                pq.pop();
            }

            int curr = pq.top().first;

            if (ans.empty() || ans.back()[1] != curr) {
                ans.push_back({x, curr});
            }
        }

        return ans;
    }
};
