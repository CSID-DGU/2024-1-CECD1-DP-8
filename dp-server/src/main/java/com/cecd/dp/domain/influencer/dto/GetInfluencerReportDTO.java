package com.cecd.dp.domain.influencer.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Builder
public class GetInfluencerReportDTO {

    private ProfileProjection profile;
    private List<MostPostsProjection> mostThreePosts;
    private List<String> allTagsOfMedias;
    private List<Float> reactionQuotient;
    private Float currentWeekLikeAvg;
    private Float currentWeekCommentsAvg;
    private Float likeAvg;
    private Float commentsAvg;
    private Float adMediaRatio;
    private Float reelsRatio;


}
