package com.cecd.dp.domain.api.report.dto.response;

import com.cecd.dp.domain.api.report.dto.ReportTagDto;
import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.media.entity.Media;

import java.util.List;
import java.util.stream.Collectors;

public record ReportTagResponseDto(
        List<ReportTagDto> tags
) {

    // 특정 인플루언서의 모든 게시물의 서로 다른 해시태그 name 반환
    public static ReportTagResponseDto fromMediaList(List<Media> mediaList) {
        List<ReportTagDto> collect = mediaList.stream()
                .flatMap(media -> media.getMediaHashTagList().stream()) // 각 미디어의 해시태그 리스트를 스트림으로 변환하고 합침
                .map(mediaHashTag -> ReportTagDto.builder()
                        .name(mediaHashTag.getHashTag().getName())
                        .build()
                )
                .distinct()
                .collect(Collectors.toList());

        return new ReportTagResponseDto(collect);
    }
}
