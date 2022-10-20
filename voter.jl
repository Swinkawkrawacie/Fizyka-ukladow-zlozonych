using Random

function mw_mcs(S, ::Val{N}, b) where N
    op_count=0
    @fastmath while op_count<N
        op_count += 1
        i = rand(1:N)
        x = rand()
        S[i] = x<0.5 ? S[b[i]] : S[b[i+2]]
    end
    return S
end

function alg_mw(S, ::Val{N}, x, b) where N
    S = shuffle(S)
    op_count = 0
    S_sum = sum(S)
    while abs(S_sum)!=N
        @fastmath S = mw_mcs(S, Val(N), b)
        op_count += 1
        S_sum = sum(S)
    end
    p = S_sum == N ? 1 : 0
    return p, op_count
end

function gen_mw(::Val{N}, L, dx) where N
    b = collect(1:N)
    b = pushfirst!(b,N)
    b = push!(b,1)
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
end

function gen_txt(::Val{N}, L, delta_x) where N
    new_delta = [collect(((i-1)*19+1)*delta_x:delta_x:(i)*19*delta_x) for i in 1:2]
    push!(new_delta, collect(39*delta_x:delta_x:1))
    results = Matrix{Float64}[]
    Threads.@threads for i = new_delta
        for j in i
        push!(results,gen_mw.(Val(N), L, round(j,digits=2)))
        end
    end
    open("N"*string(N)*"dx"*string(delta_x)*"L"*string(L)*"k.txt","a") do file
        for i in results
                write(file, string(i[1])*"  "*string(i[2])*"  "*string(i[3])*"\n")
        end
    end
end