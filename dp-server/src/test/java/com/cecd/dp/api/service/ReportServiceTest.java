package com.cecd.dp.api.service;

import com.cecd.dp.domain.api.report.dto.response.ReportResponseDto;
import com.cecd.dp.domain.api.report.service.ReportService;
import com.cecd.dp.domain.hashtag.entity.HashTag;
import com.cecd.dp.domain.hashtag.repository.HashTagRepository;
import com.cecd.dp.domain.image.ImageRepository;
import com.cecd.dp.domain.image.entity.Image;
import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.influencer.repository.InfluencerRepository;
import com.cecd.dp.domain.media.entity.Media;
import com.cecd.dp.domain.media.repository.MediaRepository;
import com.cecd.dp.domain.mediahashtag.entity.MediaHashTag;
import com.cecd.dp.domain.mediahashtag.repository.MediaHashTagRepository;
import com.cecd.dp.domain.mediahashtag.repository.impl.MediaHashTagRepositoryCustomImpl;
import com.cecd.dp.domain.meta.entity.Meta;
import com.cecd.dp.domain.meta.repository.MetaRepository;
import com.cecd.dp.type.AccountType;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDateTime;

@SpringBootTest
class ReportServiceTest {


    // 서비스 레이어
    @Autowired
    private ReportService reportService;

    // 레포지토리 레이어
    @Autowired
    private InfluencerRepository influencerRepository;

    @Autowired
    private MediaRepository mediaRepository;

    @Autowired
    private MetaRepository metaRepository;

    @Autowired
    private ImageRepository imageRepository;

    @Autowired
    private MediaHashTagRepository mediaHashTagRepository;

    // ETC..

    @BeforeEach
    void clean() {
        // 레포지토리 클리닝 작업
        influencerRepository.deleteAll();
    }

    @Test
    @DisplayName("[서비스]인플루언서 리포트 조회")
    public void 인플루언서_리포트_조회() throws Exception {
        //given
        Influencer user = Influencer.builder()
                .nickname("별명")
                .name("이름")
                .category("블로그")
                .graphId("123456789")
                .email("ovg07047@naver.com")
                .accountType(AccountType.GENERAL)
                .password("1234")
                .build();

        Media media = Media.builder()
                .caption("본문")
                .likeCnt(108)
                .replyCnt(50)
                .type("일반")
                .graphMediaId("111111111")
                .postedAt(LocalDateTime.now())
                .build();

        Image image = Image.builder()
                .imageURL("url.jpg")
                .build();

        Meta meta = Meta.builder()
                .replyAvg(20)
                .likeAvg(100)
                .followerCnt(350)
                .build();

        HashTag tag = HashTag.builder()
                .name("개발")
                .build();

        /*
        TODO: 이 부분을 서비스 로직에 넣는게 뭔가 어색하다..
         */
        MediaHashTag mediaHashTag = new MediaHashTag();
        mediaHashTag.setHashTag(tag); //TODO: 해시태그 어떻게 연관관계 매핑할까? Media에서 설정해주는게 나을 것 같은데
        mediaHashTag.setMedia(media);

        user.addMeta(meta);
        media.addImage(image);
        user.addMedia(media);

        influencerRepository.save(user);
/*        metaRepository.save(meta);
        mediaHashTagRepository.save(mediaHashTag);
        mediaRepository.save(media);
        imageRepository.save(image);*/

        //when
        ReportResponseDto report = reportService.getReport(user.getId());

        //then
        Assertions.assertEquals("이름", report.profile().name());
    }
}
