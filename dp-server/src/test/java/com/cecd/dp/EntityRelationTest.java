package com.cecd.dp;

import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.influencer.repository.InfluencerRepository;
import com.cecd.dp.domain.media.entity.Media;
import com.cecd.dp.domain.media.repository.MediaRepository;
import com.cecd.dp.type.AccountType;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
public class EntityRelationTest {

    @Autowired
    InfluencerRepository influencerRepository;

    @Autowired
    MediaRepository mediaRepository;

    @BeforeEach
    void clean(){
        influencerRepository.deleteAll();
    }

    @Test
    @DisplayName("Influencer와 Media 연관관계 설정")
    @Transactional
    public void 연관관계_설정() {
        Influencer influencer1 = Influencer.builder()
                .nickname("닉네임")
                .name("이름")
                .category("블로거")
                .graphId("123456789")
                .email("이메일")
                .accountType(AccountType.GENERAL)
                .password("비밀번호")
                .build();
        influencerRepository.save(influencer1);

        Media media1 = Media.builder()
                .caption("본문내용")
                .likeCnt(10)
                .replyCnt(24)
                .type("일반")
                .graphMediaId("987654321")
                .build();
        influencer1.addMedia(media1);
        mediaRepository.save(media1);

        Influencer influencer = influencerRepository.findById(influencer1.getId()).get();

        // 필드 값 비교
        assertThat(influencer.getNickname()).isEqualTo(influencer1.getNickname());
        assertThat(influencer.getName()).isEqualTo(influencer1.getName());
        assertThat(influencer.getCategory()).isEqualTo(influencer1.getCategory());
        assertThat(influencer.getGraphId()).isEqualTo(influencer1.getGraphId());
        assertThat(influencer.getEmail()).isEqualTo(influencer1.getEmail());
        assertThat(influencer.getAccountType()).isEqualTo(influencer1.getAccountType());
        assertThat(influencer.getPassword()).isEqualTo(influencer1.getPassword());

        influencer.getMediaList().stream()
                .forEach(
                        c ->
                                assertThat(c.getCaption()).isEqualTo(media1.getCaption())
                );
    }
}
