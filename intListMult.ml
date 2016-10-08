let multFunc lst = (List.fold_left (fun acc xs ->  [(List.fold_left 
(fun acc2 xs2 -> if (snd acc2)=(snd acc) then ((fst acc2),(snd acc2)+1) else ((fst acc2)*xs2,(snd acc2)+1)) (1,0) xs
)]::(fst acc),((snd acc)+1)) ([],0) lst)



let multFunc2 lst = List.fold_left (fun acc xs -> )