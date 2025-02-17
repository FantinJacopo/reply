/*

Code for problem C by cookiedoth
Generated 09 Mar 2023 at 10.28 AM
The Moon is Waning Gibbous (96% of Full)


   ,##.                   ,==.
 ,#    #.                 \ o ',
#        #     _     _     \    \
#        #    (_)   (_)    /    ; 
 `#    #'                 /   .'  
   `##'                   "=="

¯\_(ツ)_/¯
o_O
-_-

*/

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <functional>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <complex>
#include <cassert>
#include <random>
#include <cstring>
#include <numeric>
#include <random>
#include <utility>
#include <tuple>
#include <chrono>
#include <array>
#define ll long long
#define ld long double
#define null NULL
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define debug(a) cerr << #a << " = " << a << endl
#define forn(i, n) for (int i = 0; i < n; ++i)
#define length(a) (int)a.size()

using namespace std;

template<class T> int chkmax(T &a, T b) {
	if (b > a) {
		a = b;
		return 1;
	}
	return 0;
}

template<class T> int chkmin(T &a, T b) {
	if (b < a) {
		a = b;
		return 1;
	}
	return 0;
}

template<class iterator> void output(iterator begin, iterator end, ostream& out = cerr) {
	while (begin != end) {
		out << (*begin) << " ";
		begin++;
	}
	out << endl;
}

template<class T> void output(T x, ostream& out = cerr) {
	output(x.begin(), x.end(), out);
}

void fast_io() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
}

const int MAX_G = 55;
const int INF = 1e9;
int W, H, F, G, case_id;
vector<pair<int, int>> coords;

void case_stuff() {
	cout << "Case #" << case_id << ": ";
}

ll connect[MAX_G];

bool bruteforce(ll used, int pos, int cnt) {
	if (cnt >= F) {
		return true;
	} else if (G - pos < F - cnt) {
		return false;
	} else if ((used >> pos) & 1) {
		return bruteforce(used, pos + 1, cnt);
	} else {
		return bruteforce(used | connect[pos], pos + 1, cnt + 1) ||
			bruteforce(used, pos + 1, cnt);
	}
}

bool check(int d) {
	for (int i = 0; i < G; ++i) {
		connect[i] = 0;
	}
	for (int i = 0; i < G; ++i) {
		for (int j = 0; j < G; ++j) {
			if (abs(coords[i].first - coords[j].first) + abs(coords[i].second - coords[j].second) < d) {
				connect[i] |= (1LL << j);
			}
		}
	}
	bool res = bruteforce(0, 0, 0);
	return res;
}

void solve() {
	cin >> W >> H >> F >> G;
	cerr << "test " << G << ' ' << F << '\n';
	coords.resize(G);
	for (int i = 0; i < G; ++i) {
		cin >> coords[i].first >> coords[i].second;
	}
	int L = 0, R = W + H;
	while (L < R) {
		int mid = (L + R) >> 1;
		if (check(mid + 1)) {
			L = mid + 1;
		} else {
			R = mid;
		}
	}
	case_stuff();
	cout << L << '\n';
}

signed main() {
	fast_io();
	int T;
	cin >> T;
	for (case_id = 1; case_id <= T; ++case_id) {
		solve();
	}
}
