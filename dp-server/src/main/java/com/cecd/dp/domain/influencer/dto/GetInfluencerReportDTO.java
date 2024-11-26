package com.cecd.dp.domain.influencer.dto;

import com.cecd.dp.domain.media.dto.MediaChartProjection;
import java.util.List;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class GetInfluencerReportDTO {

  private ProfileProjection profile;
  private List<MostPostsProjection> mostThreePostsCodes;
  private List<String> allTagsOfMedias;
  private List<Float> reactionQuotient;
  private Float currentWeekLikeAvg;
  private Float currentWeekCommentsAvg;
  private Float likeAvg;
  private Float commentsAvg;
  private Float adMediaRatio;
  private Float reelsRatio;
  private List<MediaChartProjection> reelsChartComments;
  private List<MediaChartProjection> reelsChartLikes;
  private List<FollowerChartProjection> followerCharts;

  //TODO
  private Integer feedCnt;
  private Integer reelsCnt;
  private Integer adCnt;
  private Integer nonAdCnt;
  private Double commentsAvgOfAdMedia;
  private Double likeAvgOfAdMedia;

  //TODO
  @Getter
  @Setter
  public static class HashTagInfoDTO {

    private List<MostUsedHashTag> mostUsedHashTags;
    private List<EngagementAverage> engagementAverages;
    private List<EngagementMax> engagementMaxes;
    private List<EngagementTotal> engagementTotals;
    private List<HashTags> allHashTags;

    @Getter
    @Setter
    public static class MostUsedHashTag {
      private String hashTag;
      private Integer usageCount;
    }

    @Getter
    @Setter
    public static class EngagementAverage {
      private String hashTag;
      private Integer avgEngagement;
    }
    @Getter
    @Setter
    public static class EngagementMax {
      private String hashTag;
      private Integer maxEngagement;
    }
    @Getter
    @Setter
    public static class EngagementTotal {
      private String hashTag;
      private Integer totalEngagement;
    }
    @Getter
    @Setter
    public static class HashTags {
      private String hashTag;
    }
  }
}
