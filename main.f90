module mod 
integer no_atoms ! the no of atoms 
real*8 ,allocatable,dimension(:,:) :: xyz ! the xyz coordinates of the atoms 
real*8 ,allocatable,dimension(:) :: A ! mass numbers of the atoms 
real*8 ,allocatable,dimension(:) :: Z ! atomic numbers of the atoms
real*8 ,allocatable,dimension(:) :: grad ! the gradient calculated from gaussian
contains 
   subroutine foo 
	integer :: i,j
	do i=1,no_atoms
		do j=1,3
                xyz(i,j) = xyz(i,j) + 2 ! find the new coordinates
		! also use the gradient to perform the md calculations		
		end do
	end do
   end subroutine foo
end module mod 
