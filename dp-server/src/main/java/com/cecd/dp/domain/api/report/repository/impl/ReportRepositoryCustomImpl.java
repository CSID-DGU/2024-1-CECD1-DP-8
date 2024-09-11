/*
package com.cecd.dp.domain.api.report.repository.impl;

import com.cecd.dp.domain.api.report.dto.ReportMediaDto;
import com.cecd.dp.domain.api.report.dto.response.ReportMediaResponseDto;
import com.cecd.dp.domain.api.report.repository.ReportRepositoryCustom;
import com.cecd.dp.domain.influencer.entity.QInfluencer;
import com.cecd.dp.domain.media.entity.Media;
import com.querydsl.core.types.Projections;
import com.querydsl.jpa.impl.JPAQueryFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import static com.cecd.dp.domain.image.entity.QImage.image;
import static com.cecd.dp.domain.influencer.entity.QInfluencer.influencer;
import static com.cecd.dp.domain.media.entity.QMedia.media;

@Repository
@RequiredArgsConstructor
public class ReportRepositoryCustomImpl implements ReportRepositoryCustom {

    private final JPAQueryFactory jpaQueryFactory;


    // 좋아요수와 댓글수의 합이 높은 미디어 3개를 조회합니다.
    @Override
    public ReportMediaResponseDto getReportMedias(Long influencerId) {
        List<ReportMediaDto> fetch = jpaQueryFactory.select(Projections.fields(ReportMediaDto.class,
                        media.id,
                        image.imageURL, // image 필드
                        media.likeCnt,
                        media.replyCnt))
                .from(media)
                .join(media.influencer, influencer)
                .join(media.imageList, image) // media.images를 통해 image와 조인
                .offset(0)
                .limit(3)
                .orderBy(media.replyCnt.add(media.likeCnt).desc())
                .where(media.influencer.id.eq(influencerId))
                .fetch();


        return new ReportMediaResponseDto(fetch);
    }
}
*/
