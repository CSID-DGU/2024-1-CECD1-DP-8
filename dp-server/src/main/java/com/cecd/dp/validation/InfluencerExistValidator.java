package com.cecd.dp.validation;

import com.cecd.dp.domain.influencer.repository.InfluencerRepository;
import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;

public class InfluencerExistValidator implements ConstraintValidator<IsExistInfluencer, Long> {

  private InfluencerRepository influencerRepository;

  public InfluencerExistValidator(InfluencerRepository influencerRepository) {
    this.influencerRepository = influencerRepository;
  }

  @Override
  public void initialize(IsExistInfluencer constraintAnnotation) {}

  @Override
  public boolean isValid(Long influencerId, ConstraintValidatorContext context) {
    if (influencerId == null) {
      return true;
    }

    boolean isValid = influencerRepository.findById(influencerId).isPresent();
    if (!isValid) {
      context.disableDefaultConstraintViolation();
      context
          .buildConstraintViolationWithTemplate("There is no exist influencerId : " + influencerId)
          .addConstraintViolation();
    }
    return isValid;
  }
}
