simplilearnReview="""Simplilearn’s AI/ML course helped me upskill and become a Module Lead in IBM with a 50 pay raise."""
#print(simplilearnReview)

print(
      " %(edtech)s %(course)s course helped me upskill and become a Module Lead in IBM with a %(persent)d persent pay raise "
    %{
        'edtech':'Simplilearn',
        'course':'AI/ML',
        'persent':50,

     }
)

print(
      " %(edtech)s %(course)s course helped me upskill and become a Module Lead in IBM with a %(persent)d persent pay raise "
    %{
        'edtech':'MY Simplilearn',
        'course':'Generative AIL',
        'persent':100,

     }
)