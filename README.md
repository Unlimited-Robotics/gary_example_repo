================================ Example Repo ================================

This is an example of how a repo should look like. Every repo has the following
structure - 

  * components (dir): includes all of the components within that repo.
    A component is essentialy a docker container. Each component includes its 
    docker data, docker files, and bash commands to run when the container is 
    initiated. It also contains a yaml file, sharing a name with the component.
    (E.g., example_component would have example_component.yaml). The yaml file
    specifies all of the repos and ros packages the component is using, so they
    must be installed in order to use the component.
 
  * ros packages (each package has its own directory): These are the actual
    packages that the group includes (E.g., the repo gary_core_cv includes the
    ros packages gary_cv, gary_cv_bringup, gary_cv_models_cpp, gary_cv_msgs,
    and so on. They're all CV related packages, so they're grouped together in
    the same repo).

  * manifest (yaml): Just like each component has a yaml with dependencies,
    each repo has a manifest file, specifying the repos its dependent on and
    their versions. The last line in this yaml specifies the version of the
    repo itself.
 
 
