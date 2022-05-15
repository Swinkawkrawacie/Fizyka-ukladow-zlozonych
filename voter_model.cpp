#include <iostream>
#include <cstdlib>

using namespace std;

double mw_mcs(double S, int N, double b){
    int op_count=0;
    while (op_count<N){
        op_count += 1;
        int i = rand() % N;
        if (float(rand())/float((RAND_MAX))<0.5){
            S[i] = S[b[i]];
        }
        else{
            S[i] = S[b[i+2]];
        }
    }
    return S;
}

double alg_mw(double S, int N, double x, double b){
    S = random_shuffle(S.begin(),S.end());
    int op_count = 0;
    int S_sum = sum(S);
    while (abs(S_sum)!=N){
        S = mw_mcs(S, Val(N), b);
        op_count += 1;
        S_sum = sum(S);
    }
    if (S_sum == N){
        return 1, op_count;
    }
    else{
        return 0, op_count;
    }
}

double gen_mw(N, L, dx){
    double b[] = 
    b = pushfirst!(b,N)
    b = push!(b,1)
    results = Matrix{Float64}[]
    println(dx)
    time = 0
    prob = 0
    Np = floor(Int, dx*N)
    for i in 1:L
        S = vcat(fill(1,Np),fill(-1,N-Np))
        @fastmath p,t = alg_mw(S, Val(N), dx, b)
        prob += p
        time += t
    end
    time /= L
    prob /= L
    return [dx prob time]
}

function gen_txt(::Val{N}, L, delta_x) where N
    new_delta = collect(0:delta_x:1)
    results = gen_mw.(Val(N), L, new_delta)
    open("N"*string(N)*"dx"*string(delta_x)*"L"*string(L)*"e.txt","a") do file
        for i in results
            write(file, string(i[1])*"  "*string(i[2])*"  "*string(i[3])*"\n")
        end
    end
end

int main(){

}