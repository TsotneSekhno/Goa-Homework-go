// // 1. ** მისალმების ფუნქცია **
// //  შექმენით ფუნქცია `greet`, რომელიც მიიღებს სახელს პარამეტრად და მიესალმება ადამიანს.
//  თუ სახელი არ არის მოწოდებული, ნაგულისხმევი სახელი უნდა იყოს „სტუმარი“.

// // 2. ** დამატება ნაგულისხმევი პარამეტრებით **
// //  დაწერეთ ფუნქცია `დამატეთ_რიცხვები` რომელიც მიიღებს ორ რიცხვს და აბრუნებს 
// მათ ჯამს. მეორე რიცხვს უნდა ჰქონდეს ნაგულისხმევი მნიშვნელობა 0.

// // 3. **მართკუთხედის ფართობის კალკულატორი **
// //  შექმენით ფუნქცია `calculate_area` მართკუთხედის ფართობის საპოვნელად.
//  მას უნდა ჰქონდეს ორი პარამეტრი: სიგრძე და სიგანე. თუ სიგანე არ არის მოწოდებული, გამოიყენეთ
//   ნაგულისხმევი მნიშვნელობა 1.

// // 4. **ტემპერატურული კონვერტაცია**
// //  დაწერეთ ფუნქცია `convert_temperature` ტემპერატურის გადასაყვანად ცელსიუსსა
//  და ფარენჰეიტს შორის. მას უნდა ჰქონდეს ორი პარამეტრი: ტემპერატურა და მასშტაბი 
//  (ან "C" ცელსიუსზე ან "F" ფარენჰეიტისთვის), ნაგულისხმევი მასშტაბით "C".

// // 5. **საყიდლების სია **
// //  შექმენით ფუნქცია `დამატება_საყიდლების_ სიაში~, რომელიც მიიღებს საქონელს 
// და რაოდენობას. რაოდენობა ნაგულისხმევად უნდა იყოს 1, თუ არ არის მოწოდებული.

// // 6. ** დენის ფუნქცია **
// //  დაწერეთ ფუნქცია "ძალა", რომელიც ითვლის რიცხვის სიმძლავრის ნაგულისხმევი
//  მაჩვენებლის მნიშვნელობით 2 (ე.ი. კვადრატი).

// // 7. **პერსონალიზებული შეტყობინება **
// //  შექმენით ფუნქცია `create_message`, რომელიც გამოიმუშავებს პერსონალიზებულ
//  შეტყობინებას სახელწოდებით და არასავალდებულო მისალმებით ("Hello" როგორც ნაგულისხმევი).

// // 8. **გამოთვალეთ ფასდაკლება **
// //  დაწერეთ ფუნქცია `apply_discount`, რომელიც ითვლის პროდუქტის საბოლოო 
// ფასს ფასდაკლების გამოყენების შემდეგ. ფასდაკლება უნდა იყოს ნაგულისხმევი 10%.

// // 9. **შესავალი ფუნქცია**
// //  შექმენით ფუნქცია "introduce", რომელიც იღებს სახელს, ასაკს და ქვეყანას. თუ 
// ასაკი და ქვეყანა არ არის მოწოდებული, ისინი ნაგულისხმევად უნდა იყოს „უცნობი“.

// // 10. ** საბოლოო ფასის გამოთვლა **
// //  დაწერეთ ფუნქცია `გამოთვალეთ_ფასი`, რომელიც იღებს საქონლის ფასს და
//  გაყიდვების გადასახადს. გაყიდვების გადასახადი უნდა იყოს 5%.
// // 11. **იპოვე მაქსიმუმი**
// //  შექმენით ფუნქცია `find_max`, რომელიც მიიღებს სამ რიცხვს და აბრუნებს
//  ყველაზე დიდს შედარების ოპერატორების და if-else განცხადებების გამოყენებით.

// // 12. ** გაიარეთ ან ვერ გაიარეთ **
// //  დაწერეთ ფუნქცია `გადავლება_ან_ჩავარდნა` რომელიც მიიღებს მოსწავლის
//  ქულას და აბრუნებს "გადასვლას", თუ ქულა 50-ზე მეტია, ხოლო "ვერ" სხვა შემთხვევაში.

// // 13. **რიცხვების ჯამი**
// //  დაწერეთ ფუნქცია `რიცხვების_ჯამობა` რომელიც იღებს რიცხვების სიას და 
// აბრუნებს მათ ჯამს for loop-ის გამოყენებით.

// // 14. **დათვალე ლუწი რიცხვები**
// //  შექმენით ფუნქცია `count_evens`, რომელიც მიიღებს მთელი რიცხვების სიას 
// და აბრუნებს ლუწი რიცხვების რაოდენობას for loop-ის გამოყენებით.

function greet(guest){
    console.log("hello"+ guest)
}
console.log("tsotne")