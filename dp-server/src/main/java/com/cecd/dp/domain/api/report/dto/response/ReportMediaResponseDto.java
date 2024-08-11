package com.cecd.dp.domain.api.report.dto.response;

import com.cecd.dp.domain.api.report.dto.ReportMediaDto;
import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.media.entity.Media;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public record ReportMediaResponseDto(
        /*
        [인기 미디어 리스트]
        - mediaID
        - imageURL
        - likeCnt
        - replyCnt
         */
        List<ReportMediaDto> reportMedias
) {

    public static List<ReportMediaDto> toPopularMedias(List<Media> mediaList) {
        List<ReportMediaDto> popularMedias = mediaList.stream()
                .sorted(Comparator.comparingInt(
                        (Media m) -> m.getLikeCnt() + m.getReplyCnt()
                ).reversed())
                .map(media -> ReportMediaDto.builder()
                        .mediaId(media.getId())
                        .likeCnt(media.getLikeCnt())
                        .replyCnt(media.getReplyCnt())
                        .imageURL(media.getImageList().get(0).getImageURL())
                        .build())
                .collect(Collectors.toList());

        return popularMedias;
    }

    public static ReportMediaResponseDto fromMediaList(List<Media> mediaList) {
        return new ReportMediaResponseDto(toPopularMedias(mediaList));
    }
}
