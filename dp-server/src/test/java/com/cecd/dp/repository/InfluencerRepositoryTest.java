package com.cecd.dp.repository;

import static org.assertj.core.api.Assertions.assertThat;

import com.cecd.dp.domain.influencer.dto.MostPostsProjection;
import com.cecd.dp.domain.influencer.dto.ProfileProjection;
import com.cecd.dp.domain.influencer.repository.InfluencerRepository;
import jakarta.transaction.Transactional;
import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.PageRequest;

@SpringBootTest
@Transactional
public class InfluencerRepositoryTest {

  @Autowired private InfluencerRepository influencerRepository;

  @Test
  @DisplayName("getProfileById 1개만 조회 테스트")
  public void test0() throws Exception {
    // given
    Long influencerId = 1L;

    // when
    List<ProfileProjection> result =
        influencerRepository.getProfileById(influencerId, PageRequest.of(0, 1));

    // then
    assertThat(result.size()).isEqualTo(1);
  }

  @Test
  @DisplayName("getMostPostsById 3개만 조회 테스트")
  public void test1() throws Exception {
    // given
    Long influencerId = 1L;

    // when
    List<MostPostsProjection> result =
        influencerRepository.getMostThreePostsById(influencerId, PageRequest.of(0, 3));

    // then
    assertThat(result.size()).isEqualTo(3);
  }

  @Test
  @DisplayName("getAllTagNamesById 태그가 1개 이상 존재 테스트")
  public void test2() throws Exception {
    // given
    Long influencerId = 1L;

    // when
    List<String> result = influencerRepository.getAllTagNamesById(influencerId);

    // then
    assertThat(result).isNotEmpty();
    assertThat(result.size()).isGreaterThan(0);
  }

  @Test
  @DisplayName("getCurrentSevenLikeAvgById가 음수가 아님 테스트")
  public void test3() throws Exception {
    // given
    Long influencerId = 1L;

    // when
    Float result = influencerRepository.getCurrentWeekLikeAvgById(influencerId);

    System.out.println(result);
    assertThat(result).isPositive();
  }
}
