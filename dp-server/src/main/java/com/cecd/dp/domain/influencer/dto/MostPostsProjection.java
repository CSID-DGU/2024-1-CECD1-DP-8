package com.cecd.dp.domain.influencer.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class MostPostsProjection {

    private String thumbnailUrl;
    private Integer likeCnt;
    private Integer commentsCnt;

    public MostPostsProjection(String thumbnailUrl, Integer likeCnt, Integer commentsCnt) {
        this.thumbnailUrl = thumbnailUrl;
        this.likeCnt = likeCnt;
        this.commentsCnt = commentsCnt;
    }
}
