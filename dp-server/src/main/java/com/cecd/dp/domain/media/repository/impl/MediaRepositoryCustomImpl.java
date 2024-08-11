package com.cecd.dp.domain.media.repository.impl;

import com.cecd.dp.domain.media.entity.QMedia;
import com.cecd.dp.domain.media.repository.MediaRepositoryCustom;
import com.querydsl.core.types.dsl.NumberExpression;
import com.querydsl.jpa.impl.JPAQueryFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.List;

import static com.cecd.dp.domain.media.entity.QMedia.media;
@Repository
@RequiredArgsConstructor
public class MediaRepositoryCustomImpl implements MediaRepositoryCustom {

    private final JPAQueryFactory jpaQueryFactory;

    @Override
    public Float calculateMediaUploadCycle(Long influencerId) {
        LocalDateTime now = LocalDateTime.now();

        NumberExpression<Integer> weekOfYear = media.createdAt.yearWeek();

        // 주별로 게시물 수 계산
        List<Long> weeklyUploads = jpaQueryFactory
                .select(media.count())
                .from(media)
                .where(media.influencer.id.eq(influencerId)
                        .and(media.createdAt.between(now.minus(1, ChronoUnit.YEARS), now)))
                .groupBy(weekOfYear)
                .fetch();

        long totalUploads = weeklyUploads.stream().mapToLong(Long::longValue).sum();

        int numberOfWeeks = weeklyUploads.size();

        if (numberOfWeeks == 0) {
            return 0f;
        }

        return (float)totalUploads / numberOfWeeks;
    }
}
