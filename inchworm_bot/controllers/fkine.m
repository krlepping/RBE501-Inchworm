function T = fkine(S,M,q,frame) % If frame = true, body, else space
    if frame == "body"
        T = M;
        for i = 1:length(S(1,:))
            T = T * twist2ht(S(:,i),q(i));
        end
    end
    if frame == "space"
        T = 1;
        for i = 1:length(S(1,:))
            T = T * twist2ht(S(:,i),q(i));
        end
        T = T * M;
    end
end