package com.cecd.dp.domain.api.report.dto.response;

import com.cecd.dp.domain.influencer.entity.Influencer;
import lombok.Builder;

@Builder
public record ReportProfileResponseDto(
        String nickname,        // 인스타 별칭
        String name,            // 인스타 이름
        Integer mediaCnt,       // 게시글 수
        Integer followerCnt    // 팔로워 수
/*TODO:
        Integer influenceScore, // 영향력 지수
        Integer adScore         // 광고 지수*/
) {

    public static ReportProfileResponseDto fromInfluencer(Influencer influencer) {
        return ReportProfileResponseDto.builder()
                .nickname(influencer.getNickname())
                .name(influencer.getName())
                .mediaCnt(influencer.getMediaCnt())
                .followerCnt(influencer.getLatestMeta().getFollowerCnt())
                // 영향력 지수
                // 광고 지수
                .build();
    }
}
