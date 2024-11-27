package com.cecd.dp.domain.influencer.dto;

import java.util.List;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class GetHashTagReportDTO {
  private List<UsageCount> usageCounts;
  private List<AvgEngagement> avgEngagements;
  private List<MaxEngagement> maxEngagements;
  private List<TotalEngagement> totalEngagements;

  @Getter
  @Setter
  @Builder
  public static class UsageCount {
    private String hashTag;
    private Integer usageCount;
  }

  @Getter
  @Setter
  @Builder
  public static class AvgEngagement {
    private String hashTag;
    private Integer avgEngagement;
  }

  @Getter
  @Setter
  @Builder
  public static class MaxEngagement {
    private String hashTag;
    private Integer maxEngagement;
  }

  @Getter
  @Setter
  @Builder
  public static class TotalEngagement {
    private String hashTag;
    private Integer totalEngagement;
  }
}
