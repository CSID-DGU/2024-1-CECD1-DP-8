/*
package com.cecd.dp.domain.api.report.repository.impl;

import com.cecd.dp.domain.api.report.dto.ReportTagDto;
import com.cecd.dp.domain.api.report.dto.response.ReportTagResponseDto;
import com.cecd.dp.domain.api.report.dto.response.SummaryResponseDto;
import com.cecd.dp.domain.api.report.repository.ReportHashTagRepositoryCustom;
import com.cecd.dp.domain.mediahashtag.entity.QMediaHashTag;
import com.querydsl.core.types.Projections;
import com.querydsl.jpa.impl.JPAQueryFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Optional;

import static com.cecd.dp.domain.hashtag.entity.QHashTag.hashTag;
import static com.cecd.dp.domain.influencer.entity.QInfluencer.influencer;
import static com.cecd.dp.domain.media.entity.QMedia.media;
import static com.cecd.dp.domain.mediahashtag.entity.QMediaHashTag.mediaHashTag;

@Repository
@RequiredArgsConstructor
public class ReportHashTagRepositoryCustomImpl implements ReportHashTagRepositoryCustom {


    private final JPAQueryFactory jpaQueryFactory;
    @Override
    public ReportTagResponseDto getAllDistinctTagList(Long influencerId) {
        List<ReportTagDto> fetch = jpaQueryFactory.select(Projections.fields(
                        ReportTagDto.class,
                        hashTag.name
                ))
                .from(influencer)
                .join(influencer.mediaList, media) // influencer와 media를 조인
                .join(media.mediaHashTagList, mediaHashTag) // media와 mediaHashTag를 조인
                .join(mediaHashTag.hashTag, hashTag) // mediaHashTag와 hashTag를 조인
                .where(influencer.id.eq(influencerId))
                .distinct()
                .fetch();

        return new ReportTagResponseDto(fetch);
    }
}
*/
